#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
market = json.loads((root / "config/marketplace-policy.json").read_text())
payment = json.loads((root / "config/payment-policy.json").read_text())

checks = {
    "versioned API": market.get("apiBase", "").startswith("/api/v1/"),
    "authentication": market.get("authenticationRequired") is True,
    "tenant isolation": market.get("tenantIsolation") == "server-authoritative",
    "English and Tamil": {"en-GB", "ta"}.issubset(set(market.get("supportedLocales", []))),
    "seller verification": market.get("sellerVerificationRequired") is True,
    "guardian control": market.get("minorPurchasesRequireGuardian") is True,
    "idempotency": market.get("idempotencyRequired") is True,
    "audit": market.get("auditRequired") is True,
    "price snapshot": market.get("priceCurrencyImmutableAfterOrder") is True,
    "no raw card storage": payment.get("storeRawCardData") is False,
    "provider tokenisation": payment.get("paymentProviderTokenisationRequired") is True,
    "signed webhooks": payment.get("webhookSignatureRequired") is True,
    "replay window": 0 < payment.get("webhookReplayWindowSeconds", 0) <= 600,
    "reconciliation": payment.get("settlementReconciliationRequired") is True,
}
failed = [name for name, passed in checks.items() if not passed]
for name, passed in checks.items():
    print(("PASS" if passed else "FAIL") + ": " + name)
if failed:
    raise SystemExit("Marketplace baseline failed: " + ", ".join(failed))
print("Marketplace baseline validated")
