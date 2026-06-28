from src.analytics.queries import Analytics

analytics = Analytics()

print("=" * 60)
print("TOP 10 MARKET CAP")
print("=" * 60)

print(analytics.top_market_cap())

print()

print("=" * 60)
print("AVERAGE ROE")
print("=" * 60)

print(analytics.average_roe())

analytics.close()