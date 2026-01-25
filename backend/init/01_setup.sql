-- 1. Criar Tipos ENUM primeiro
CREATE TYPE transaction_type AS ENUM ('PIX', 'BOLETO', 'TED');
CREATE TYPE transaction_status AS ENUM ('APROVADO', 'NEGADO', 'EM_PROCESSAMENTO');

-- 2. Tabela de Consumidores
CREATE TABLE Consumers (
    consumer_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(150) NOT NULL,
    birth_date DATE NOT NULL,
    income SMALLINT NOT NULL, 
    email VARCHAR(100) UNIQUE NOT NULL,
    uf CHAR(2) NOT NULL,
    city VARCHAR(100) NOT NULL, 
    register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Adicionado DEFAULT
);

-- Comentário deve vir fora do bloco CREATE TABLE
COMMENT ON COLUMN Consumers.income IS '1: 0-2k, 2: 2k-5k, 3: 5k-10k, 4: 10k+';

-- 3. Tabela de Transações
CREATE TABLE Transactions (
    transaction_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    sender_id UUID REFERENCES Consumers(consumer_id),
    receiver_id UUID REFERENCES Consumers(consumer_id),
    amount DECIMAL(15,2) NOT NULL,
    type transaction_type NOT NULL,
    transaction_at TIMESTAMP DEFAULT now(),
    currency CHAR(3) DEFAULT 'BRL',
    status transaction_status DEFAULT 'EM_PROCESSAMENTO' 
); 