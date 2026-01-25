CREATE TABLE Consumers (
    consumer_id UUID PRIMARY KEY DEFAULT gen_random_uuid(), --Observar se isso não irá sobrescrever o ID gerado no producer
    name varchar(150) NOT NULL,
    birth_date date NOT NULL,
    income smallint NOT NULL, --Range de renda
    email varchar(100) UNIQUE NOT NULL,
    uf char(2) NOT NULL,
    city = varchar(100) NOT NULL
    register_date timestamp CURRENT_TIMESTAMP
    COMMENT ON COLUMN consumers.income_range IS '1: 0-2k, 2: 2k-5k, 3: 5k-10k, 4: 10k+';
)

CREATE TYPE transaction_type AS ENUM ('PIX', 'BOLETO', 'TED');
CREATE TYPE transaction_status AS ENUM ('APROVADO', 'NEGADO', 'EM_PROCESSAMENTO');

CREATE TABLE Transactions (
    transaction_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    sender_id UUID REFERENCES Consumers(consumer_id),
    receiver_id UUID REFERENCES Consumers(consumer_id),
    amount DECIMAL(15,2) NOT NULL,
    type transaction_type NOT NULL,
    transaction_at timestamp DEFAULT now(),
    currency CHAR(3) DEFAULT 'BRL',
    status transaction_status DEFAULT "EM_PROCESSAMENTO",
)