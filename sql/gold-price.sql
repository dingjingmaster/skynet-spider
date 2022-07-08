
-- 金价/银价表

create table glod_price (
    id          VARCHAR(255) PRIMARY KEY NOT NULL,          -- 主键: 类型(au/ag)-area(CNY/USD)-timestamp(20221110)-type
    itemType    VARCHAR(32)     NOT NULL,                   -- 类型: au/ag
    area        VARCHAR(32)     NOT NULL,                   -- 地区: USD/CNY
    price       DOUBLE          NOT NULL,                   -- 价格: 数字
    time        VARCHAR(10)     NOT NULL                    -- 时间: 20221110
);
