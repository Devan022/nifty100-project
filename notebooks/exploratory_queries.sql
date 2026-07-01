-- Query 1: Show first 10 companies
SELECT *
FROM companies
LIMIT 10;

-- Query 2: Top 10 companies by market cap
SELECT company_id, year, market_cap_crore
FROM market_cap
ORDER BY market_cap_crore DESC
LIMIT 10;

-- Query 3: Average ROE
SELECT AVG(return_on_equity_pct) AS average_roe
FROM financial_ratios;

-- Query 4: Top 10 companies by sales
SELECT company_id, year, sales
FROM profitandloss
ORDER BY sales DESC
LIMIT 10;

-- Query 5: Highest operating cash flow
SELECT company_id, year, cash_from_operating_activity
FROM cashflow
ORDER BY cash_from_operating_activity DESC
LIMIT 10;

-- Query 6: Number of companies in each sector
SELECT broad_sector, COUNT(*) AS total_companies
FROM sectors
GROUP BY broad_sector
ORDER BY total_companies DESC;

-- Query 7: Highest PE ratio
SELECT company_id, year, pe_ratio
FROM market_cap
ORDER BY pe_ratio DESC
LIMIT 10;

-- Query 8: Highest dividend yield
SELECT company_id, year, dividend_yield_pct
FROM market_cap
ORDER BY dividend_yield_pct DESC
LIMIT 10;

-- Query 9: Highest ROCE
SELECT company_id, year, return_on_capital_employed_pct
FROM financial_ratios
ORDER BY return_on_capital_employed_pct DESC
LIMIT 10;

-- Query 10: Companies with highest EPS
SELECT company_id, year, eps
FROM profitandloss
ORDER BY eps DESC
LIMIT 10;