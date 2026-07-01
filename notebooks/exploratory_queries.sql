-- ==========================================
-- Query 1: Top 10 Companies by Market Cap
-- ==========================================

SELECT
    company_id,
    year,
    market_cap_crore
FROM market_cap
WHERE year = (
    SELECT MAX(year)
    FROM market_cap
)
ORDER BY market_cap_crore DESC
LIMIT 10;


-- ==========================================
-- Query 2: Average ROE
-- ==========================================

SELECT
    AVG(return_on_equity_pct) AS average_roe
FROM financial_ratios;


-- ==========================================
-- Query 3: Highest Debt to Equity
-- ==========================================

SELECT
    company_id,
    year,
    debt_to_equity
FROM financial_ratios
ORDER BY debt_to_equity DESC
LIMIT 10;


-- ==========================================
-- Query 4: Highest Net Profit
-- ==========================================

SELECT
    company_id,
    year,
    net_profit
FROM profitandloss
ORDER BY net_profit DESC
LIMIT 10;


-- ==========================================
-- Query 5: Highest Sales
-- ==========================================

SELECT
    company_id,
    year,
    sales
FROM profitandloss
ORDER BY sales DESC
LIMIT 10;


-- ==========================================
-- Query 6: Highest Operating Cash Flow
-- ==========================================

SELECT
    company_id,
    year,
    cash_from_operations_cr
FROM financial_ratios
ORDER BY cash_from_operations_cr DESC
LIMIT 10;


-- ==========================================
-- Query 7: Highest Book Value
-- ==========================================

SELECT
    id,
    book_value
FROM companies
ORDER BY book_value DESC
LIMIT 10;


-- ==========================================
-- Query 8: Companies with Lowest PE Ratio
-- ==========================================

SELECT
    company_id,
    year,
    pe_ratio
FROM market_cap
WHERE pe_ratio IS NOT NULL
ORDER BY pe_ratio ASC
LIMIT 10;


-- ==========================================
-- Query 9: Companies with Highest ROCE
-- ==========================================

SELECT
    id,
    roce_percentage
FROM companies
ORDER BY roce_percentage DESC
LIMIT 10;


-- ==========================================
-- Query 10: Companies with Highest ROE
-- ==========================================

SELECT
    id,
    roe_percentage
FROM companies
ORDER BY roe_percentage DESC
LIMIT 10;