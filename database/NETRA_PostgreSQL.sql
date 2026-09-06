
DROP TABLE IF EXISTS evidence CASCADE;
DROP TABLE IF EXISTS transactions CASCADE;
DROP TABLE IF EXISTS accounts CASCADE;
DROP TABLE IF EXISTS phones CASCADE;
DROP TABLE IF EXISTS vehicles CASCADE;
DROP TABLE IF EXISTS cases CASCADE;
DROP TABLE IF EXISTS locations CASCADE;
DROP TABLE IF EXISTS person CASCADE;



CREATE TABLE person (
    person_id VARCHAR(10) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT
);

CREATE TABLE locations (
    location_id VARCHAR(10) PRIMARY KEY,
    location_name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL
);

CREATE TABLE cases (
    case_id VARCHAR(10) PRIMARY KEY,
    crime_type VARCHAR(50) NOT NULL,
    case_date DATE,
    status VARCHAR(50),
    location_id VARCHAR(10),
    CONSTRAINT fk_case_location
        FOREIGN KEY (location_id)
        REFERENCES locations(location_id)
);

CREATE TABLE phones (
    phone_id VARCHAR(10) PRIMARY KEY,
    phone_number VARCHAR(10) UNIQUE,
    person_id VARCHAR(10),
    CONSTRAINT fk_phone_person
        FOREIGN KEY (person_id)
        REFERENCES person(person_id)
);

CREATE TABLE vehicles (
    vehicle_id VARCHAR(10) PRIMARY KEY,
    vehicle_type VARCHAR(50),
    registration_no VARCHAR(30) UNIQUE,
    person_id VARCHAR(10),
    CONSTRAINT fk_vehicle_person
        FOREIGN KEY (person_id)
        REFERENCES person(person_id)
);

CREATE TABLE accounts (
    account_id VARCHAR(10) PRIMARY KEY,
    account_type VARCHAR(30),
    owner_id VARCHAR(10),
    CONSTRAINT fk_account_owner
        FOREIGN KEY (owner_id)
        REFERENCES person(person_id)
);

CREATE TABLE transactions (
    transaction_id VARCHAR(10) PRIMARY KEY,
    sender_id VARCHAR(10),
    receiver_id VARCHAR(10),
    amount NUMERIC(12,2),
    transaction_date TIMESTAMP,
    transaction_type VARCHAR(30),
    CONSTRAINT fk_transaction_sender
        FOREIGN KEY (sender_id)
        REFERENCES person(person_id),
    CONSTRAINT fk_transaction_receiver
        FOREIGN KEY (receiver_id)
        REFERENCES person(person_id)
);

CREATE TABLE evidence (
    evidence_id VARCHAR(10) PRIMARY KEY,
    case_id VARCHAR(10),
    evidence_type VARCHAR(50),
    description TEXT,
    status VARCHAR(30),
    CONSTRAINT fk_evidence_case
        FOREIGN KEY (case_id)
        REFERENCES cases(case_id)
);



INSERT INTO person (person_id, name, age)
VALUES
('P001', 'Ravi Sharma', 32),
('P002', 'Suresh Rao', 38),
('P003', 'Anil Verma', 29),
('P004', 'Meena Kapoor', 35),
('P005', 'Arjun Singh', 41),
('P006', 'Kiran Reddy', 34),
('P007', 'Neha Patel', 28),
('P008', 'Vikram Das', 40),
('P009', 'Priya Nair', 31),
('P010', 'Rahul Mehta', 36),
('P011', 'Sneha Rao', 27),
('P012', 'Manoj Kumar', 43),
('P013', 'Asha Verma', 30),
('P014', 'Rohit Shah', 39),
('P015', 'Divya Singh', 33);



INSERT INTO locations (location_id, location_name, city)
VALUES
('L001', 'Jubilee Hills', 'Hyderabad'),
('L002', 'Banjara Hills', 'Hyderabad'),
('L003', 'Kukatpally', 'Hyderabad'),
('L004', 'Secunderabad', 'Hyderabad'),
('L005', 'Madhapur', 'Hyderabad'),
('L006', 'Gachibowli', 'Hyderabad'),
('L007', 'Ameerpet', 'Hyderabad'),
('L008', 'Begumpet', 'Hyderabad');



INSERT INTO cases
(case_id, crime_type, case_date, status, location_id)
VALUES
('C1042', 'Robbery', '2026-08-12', 'Under Investigation', 'L001'),
('C0817', 'Robbery', '2025-11-18', 'Closed', 'L002'),
('C0562', 'Robbery', '2025-05-03', 'Closed', 'L003'),
('C0301', 'Theft', '2024-09-21', 'Closed', 'L001'),
('C1205', 'Robbery', '2026-08-20', 'Under Investigation', 'L005'),
('C1210', 'Theft', '2026-08-22', 'Under Investigation', 'L006'),
('C1215', 'Fraud', '2026-08-25', 'Under Investigation', 'L007'),
('C1220', 'Robbery', '2026-08-28', 'Under Investigation', 'L005'),
('C1225', 'Theft', '2026-08-30', 'Closed', 'L008'),
('C1230', 'Fraud', '2026-09-01', 'Under Investigation', 'L006');



INSERT INTO phones (phone_id, phone_number, person_id)
VALUES
('PH001', '9678905678', 'P001'),
('PH002', '8982576687', 'P002'),
('PH003', '7867903423', 'P003'),
('PH004', '8090675932', 'P004'),
('PH005', '9876502005', 'P006'),
('PH006', '8765402006', 'P007'),
('PH007', '7654302007', 'P008'),
('PH008', '9123402008', 'P009'),
('PH009', '9988702009', 'P010'),
('PH010', '8899102010', 'P011'),
('PH011', '7766502011', 'P012'),
('PH012', '9345602012', 'P013'),
('PH013', '9654302013', 'P014'),
('PH014', '8123402014', 'P015'),
('PH015', '9234502015', 'P015');



INSERT INTO vehicles
(vehicle_id, vehicle_type, registration_no, person_id)
VALUES
('V001', 'White SUV', 'TEST-V001', 'P001'),
('V002', 'Black Sedan', 'TEST-V002', 'P002'),
('V003', 'Blue Bike', 'TEST-V003', 'P003'),
('V004', 'Black SUV', 'TEST-V004', 'P006'),
('V005', 'White Sedan', 'TEST-V005', 'P007'),
('V006', 'Grey Hatchback', 'TEST-V006', 'P008'),
('V007', 'Red Bike', 'TEST-V007', 'P010'),
('V008', 'Blue Sedan', 'TEST-V008', 'P012'),
('V009', 'Silver SUV', 'TEST-V009', 'P014'),
('V010', 'Black Bike', 'TEST-V010', 'P015');



INSERT INTO accounts
(account_id, account_type, owner_id)
VALUES
('A001', 'Savings', 'P001'),
('A002', 'Savings', 'P002'),
('A003', 'Business', 'P003'),
('A004', 'Savings', 'P006'),
('A005', 'Business', 'P007'),
('A006', 'Savings', 'P008'),
('A007', 'Savings', 'P009'),
('A008', 'Business', 'P010'),
('A009', 'Savings', 'P011'),
('A010', 'Savings', 'P012'),
('A011', 'Business', 'P013'),
('A012', 'Savings', 'P014'),
('A013', 'Savings', 'P015');



INSERT INTO transactions
(transaction_id, sender_id, receiver_id, amount, transaction_date, transaction_type)
VALUES
('T001', 'P001', 'P002', 450000.00, '2026-08-10 14:30:00', 'Digital'),
('T002', 'P003', 'P001', 120000.00, '2026-08-11 11:20:00', 'Digital'),
('T003', 'P002', 'P004', 80000.00, '2026-08-12 09:15:00', 'Digital'),
('T004', 'P006', 'P007', 175000.00, '2026-08-18 10:30:00', 'Digital'),
('T005', 'P007', 'P008', 95000.00, '2026-08-19 12:15:00', 'Digital'),
('T006', 'P008', 'P009', 210000.00, '2026-08-21 15:45:00', 'Digital'),
('T007', 'P009', 'P010', 65000.00, '2026-08-23 09:20:00', 'Digital'),
('T008', 'P010', 'P006', 320000.00, '2026-08-24 18:10:00', 'Digital'),
('T009', 'P011', 'P012', 110000.00, '2026-08-26 11:05:00', 'Digital'),
('T010', 'P012', 'P013', 275000.00, '2026-08-27 14:40:00', 'Digital'),
('T011', 'P013', 'P014', 85000.00, '2026-08-29 16:30:00', 'Digital'),
('T012', 'P014', 'P015', 190000.00, '2026-08-30 13:25:00', 'Digital'),
('T013', 'P015', 'P006', 125000.00, '2026-08-31 17:50:00', 'Digital');




INSERT INTO evidence
(evidence_id, case_id, evidence_type, description, status)
VALUES
('E001', 'C1042', 'CCTV', 'Vehicle observed near location', 'Verified'),
('E002', 'C1042', 'Witness', 'Witness reported meeting between two persons', 'Reported'),
('E003', 'C1042', 'Financial', 'Transaction associated with person network', 'Verified'),
('E004', 'C1042', 'Cash Event', 'Reported cash exchange with no digital record', 'Unverified'),
('E005', 'C1205', 'CCTV', 'Vehicle observed near incident location', 'Verified'),
('E006', 'C1210', 'Witness', 'Witness reported suspicious meeting', 'Reported'),
('E007', 'C1215', 'Financial', 'Transaction linked to investigation network', 'Verified'),
('E008', 'C1220', 'CCTV', 'Vehicle appeared near location', 'Verified'),
('E009', 'C1225', 'Witness', 'Person reported suspicious activity', 'Reported'),
('E010', 'C1230', 'Financial', 'Unusual transaction identified', 'Verified'),
('E011', 'C1205', 'Phone', 'Phone activity associated with investigation', 'Verified'),
('E012', 'C1210', 'Vehicle', 'Vehicle associated with person of interest', 'Reported'),
('E013', 'C1215', 'Document', 'Financial document submitted for review', 'Verified'),
('E014', 'C1230', 'Digital', 'Digital record requires further verification', 'Unverified');



SELECT * FROM person ORDER BY person_id;

SELECT * FROM phones ORDER BY phone_id;

SELECT * FROM vehicles ORDER BY vehicle_id;

SELECT * FROM locations ORDER BY location_id;

SELECT * FROM cases ORDER BY case_id;

SELECT * FROM accounts ORDER BY account_id;

SELECT * FROM transactions ORDER BY transaction_id;

SELECT * FROM evidence ORDER BY evidence_id;




SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
  AND table_type = 'BASE TABLE'
ORDER BY table_name;





SELECT 'person' AS table_name, COUNT(*) AS total FROM person
UNION ALL
SELECT 'phones', COUNT(*) FROM phones
UNION ALL
SELECT 'vehicles', COUNT(*) FROM vehicles
UNION ALL
SELECT 'locations', COUNT(*) FROM locations
UNION ALL
SELECT 'cases', COUNT(*) FROM cases
UNION ALL
SELECT 'accounts', COUNT(*) FROM accounts
UNION ALL
SELECT 'transactions', COUNT(*) FROM transactions
UNION ALL
SELECT 'evidence', COUNT(*) FROM evidence;



-- Phones assigned to persons
SELECT
    p.person_id,
    p.name,
    ph.phone_id,
    ph.phone_number
FROM person p
JOIN phones ph ON p.person_id = ph.person_id
ORDER BY p.person_id;

-- Vehicles assigned to persons
SELECT
    p.person_id,
    p.name,
    v.vehicle_id,
    v.vehicle_type,
    v.registration_no
FROM person p
JOIN vehicles v ON p.person_id = v.person_id
ORDER BY p.person_id;

-- Accounts owned by persons
SELECT
    p.person_id,
    p.name,
    a.account_id,
    a.account_type
FROM person p
JOIN accounts a ON p.person_id = a.owner_id
ORDER BY p.person_id;

-- Cases and their locations
SELECT
    c.case_id,
    c.crime_type,
    c.case_date,
    c.status,
    l.location_id,
    l.location_name,
    l.city
FROM cases c
JOIN locations l ON c.location_id = l.location_id
ORDER BY c.case_id;

-- Transactions with sender and receiver
SELECT
    t.transaction_id,
    s.person_id AS sender_id,
    s.name AS sender_name,
    r.person_id AS receiver_id,
    r.name AS receiver_name,
    t.amount,
    t.transaction_date,
    t.transaction_type
FROM transactions t
JOIN person s ON t.sender_id = s.person_id
JOIN person r ON t.receiver_id = r.person_id
ORDER BY t.transaction_id;

-- Evidence and related cases
SELECT
    e.evidence_id,
    e.evidence_type,
    e.status,
    e.description,
    c.case_id,
    c.crime_type
FROM evidence e
JOIN cases c ON e.case_id = c.case_id
ORDER BY e.evidence_id;




-- People involved in transactions
SELECT
    s.name AS sender,
    r.name AS receiver,
    t.amount,
    t.transaction_date
FROM transactions t
JOIN person s ON t.sender_id = s.person_id
JOIN person r ON t.receiver_id = r.person_id
ORDER BY t.amount DESC;


-- Cases by crime type
SELECT
    crime_type,
    COUNT(*) AS case_count
FROM cases
GROUP BY crime_type
ORDER BY case_count DESC;


-- Evidence count by case
SELECT
    c.case_id,
    c.crime_type,
    COUNT(e.evidence_id) AS evidence_count
FROM cases c
LEFT JOIN evidence e ON c.case_id = e.case_id
GROUP BY c.case_id, c.crime_type
ORDER BY evidence_count DESC;


-- High-value transactions
SELECT *
FROM transactions
WHERE amount >= 200000
ORDER BY amount DESC;


-- People receiving/sending multiple transactions
SELECT
    p.person_id,
    p.name,
    COUNT(t.transaction_id) AS transaction_count
FROM person p
LEFT JOIN transactions t
    ON p.person_id = t.sender_id
    OR p.person_id = t.receiver_id
GROUP BY p.person_id, p.name
ORDER BY transaction_count DESC;



