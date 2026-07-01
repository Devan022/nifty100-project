PRAGMA foreign_keys = ON;

----------------------------------------------------
-- Companies
----------------------------------------------------
CREATE TABLE IF NOT EXISTS companies (
    id TEXT PRIMARY KEY,
    company_logo TEXT,
    company_name TEXT,
    chart_link TEXT,
    about_company TEXT,
    website TEXT,
    nse_profile TEXT,
    bse_profile TEXT,
    face_value REAL,
    book_value REAL,
    roce_percentage REAL,
    roe_percentage REAL
);

----------------------------------------------------
-- Profit and Loss
----------------------------------------------------
CREATE TABLE IF NOT EXISTS profitandloss (

    id INTEGER,

    company_id TEXT,

    year TEXT,

    sales REAL,
    expenses REAL,
    operating_profit REAL,
    opm_percentage REAL,
    other_income REAL,
    interest REAL,
    depreciation REAL,
    profit_before_tax REAL,
    tax_percentage REAL,
    net_profit REAL,
    eps REAL,
    dividend_payout REAL,

    PRIMARY KEY(company_id, year),

    FOREIGN KEY(company_id)
        REFERENCES companies(id)
);

----------------------------------------------------
-- Balance Sheet
----------------------------------------------------
CREATE TABLE IF NOT EXISTS balancesheet (

    id INTEGER,

    company_id TEXT,

    year TEXT,

    equity_capital REAL,
    reserves REAL,
    borrowings REAL,
    other_liabilities REAL,
    total_liabilities REAL,
    fixed_assets REAL,
    cwip REAL,
    investments REAL,
    other_asset REAL,
    total_assets REAL,

    PRIMARY KEY(company_id, year),

    FOREIGN KEY(company_id)
        REFERENCES companies(id)
);

----------------------------------------------------
-- Cash Flow
----------------------------------------------------
CREATE TABLE IF NOT EXISTS cashflow (

    id INTEGER,

    company_id TEXT,

    year TEXT,

    operating_activity REAL,
    investing_activity REAL,
    financing_activity REAL,
    net_cash_flow REAL,

    PRIMARY KEY(company_id, year),

    FOREIGN KEY(company_id)
        REFERENCES companies(id)
);

----------------------------------------------------
-- Analysis
----------------------------------------------------
CREATE TABLE IF NOT EXISTS analysis (

    id INTEGER PRIMARY KEY,

    company_id TEXT,

    compounded_sales_growth TEXT,
    compounded_profit_growth TEXT,
    stock_price_cagr TEXT,
    roe TEXT,

    FOREIGN KEY(company_id)
        REFERENCES companies(id)
);

----------------------------------------------------
-- Documents
----------------------------------------------------
CREATE TABLE IF NOT EXISTS documents (

    id INTEGER PRIMARY KEY,

    company_id TEXT,

    year INTEGER,

    annual_report TEXT,

    FOREIGN KEY(company_id)
        REFERENCES companies(id)
);

----------------------------------------------------
-- Pros and Cons
----------------------------------------------------
CREATE TABLE IF NOT EXISTS prosandcons (

    id INTEGER PRIMARY KEY,

    company_id TEXT,

    pros TEXT,

    cons TEXT,

    FOREIGN KEY(company_id)
        REFERENCES companies(id)
);

----------------------------------------------------
-- Sectors
----------------------------------------------------
CREATE TABLE IF NOT EXISTS sectors (

    id INTEGER,

    company_id TEXT,

    broad_sector TEXT,

    sub_sector TEXT,

    index_weight_pct REAL,

    market_cap_category TEXT,

    PRIMARY KEY(company_id),

    FOREIGN KEY(company_id)
        REFERENCES companies(id)
);

----------------------------------------------------
-- Stock Prices
----------------------------------------------------
CREATE TABLE IF NOT EXISTS stock_prices (

    id INTEGER,

    company_id TEXT,

    date TEXT,

    open_price REAL,

    high_price REAL,

    low_price REAL,

    close_price REAL,

    volume INTEGER,

    adjusted_close REAL,

    PRIMARY KEY(company_id, date),

    FOREIGN KEY(company_id)
        REFERENCES companies(id)
);

----------------------------------------------------
-- Market Cap
----------------------------------------------------
CREATE TABLE IF NOT EXISTS market_cap (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id TEXT NOT NULL,
    year INTEGER NOT NULL,
    market_cap_crore REAL,
    enterprise_value_crore REAL,
    pe_ratio REAL,
    pb_ratio REAL,
    ev_ebitda REAL,
    dividend_yield_pct REAL,
    FOREIGN KEY(company_id) REFERENCES companies(company_id),
    UNIQUE(company_id, year)
);

----------------------------------------------------
-- Financial Ratios
----------------------------------------------------
CREATE TABLE IF NOT EXISTS financial_ratios (

    id INTEGER,

    company_id TEXT,

    year TEXT,

    net_profit_margin_pct REAL,

    operating_profit_margin_pct REAL,

    return_on_equity_pct REAL,

    debt_to_equity REAL,

    interest_coverage REAL,

    asset_turnover REAL,

    free_cash_flow_cr REAL,

    capex_cr REAL,

    earnings_per_share REAL,

    book_value_per_share REAL,

    dividend_payout_ratio_pct REAL,

    total_debt_cr REAL,

    cash_from_operations_cr REAL,

    PRIMARY KEY(company_id, year),

    FOREIGN KEY(company_id)
        REFERENCES companies(id)
);

----------------------------------------------------
-- Peer Groups
----------------------------------------------------
CREATE TABLE IF NOT EXISTS peer_groups (

    company_id TEXT,

    peer_group TEXT,

    benchmark_flag INTEGER,

    PRIMARY KEY(company_id),

    FOREIGN KEY(company_id)
        REFERENCES companies(id)
);