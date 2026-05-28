-- Airport Table

CREATE TABLE airport (
    airport_code CHAR(3) PRIMARY KEY CHECK(airport_code = UPPER(airport_code)),
    airport_name VARCHAR(50) NOT NULL UNIQUE,
    airport_timezone VARCHAR(60) NOT NULL,
    airport_city VARCHAR(50) NOT NULL,
    airport_country VARCHAR(50) NOT NULL,
    CONSTRAINT chk_timezone_format CHECK (airport_timezone LIKE '%/%'));

-- Passenger Table

CREATE TABLE passenger (
    passenger_id INT(10) PRIMARY KEY,
    passenger_dob DATE NOT NULL,
    passport_num VARCHAR(20) UNIQUE NOT NULL,
    passenger_nationality VARCHAR(30) NOT NULL,
    p_first_name VARCHAR(50) NOT NULL,
    p_middle_name VARCHAR(50),
    p_last_name VARCHAR(50) NOT NULL
);

-- Employee Table

CREATE TABLE employee (
    Emp_id INT(7) PRIMARY KEY CHECK(emp_id > 0),
    emp_role VARCHAR(50) NOT NULL CHECK(emp_role IN('Pilot','Flight Attendant','Baggage Handler','Ground Control','Gate Agent','Mechanic')),
    emp_first_name VARCHAR(50) NOT NULL,
    emp_last_name VARCHAR(50) NOT NULL
);

-- Gate Table

CREATE TABLE gate (
    gate_id VARCHAR(5) PRIMARY KEY,
    terminal CHAR(1) NOT NULL,
    gate_number INT(11) NOT NULL CHECK(gate_number > 0),
    CONSTRAINT unique_terminal_gate UNIQUE (terminal, gate_number)
);

-- Flight Table

    CREATE TABLE flight (
    flight_id INT(10) PRIMARY KEY,
    airline VARCHAR(50) NOT NULL,
    origin VARCHAR(50) NOT NULL,
    destination VARCHAR(50) NOT NULL,
    status VARCHAR(20) NOT NULL CHECK(status IN ('SCHEDULED','BOARDING','DEPARTED','IN_FLIGHT','ARRIVED','DELAYED','CANCELLED')),
    departure_time DATETIME NOT NULL,
    arrival_time DATETIME NOT NULL,
    departure_airport_id CHAR(3) NOT NULL,
    arrival_airport_id CHAR(3) NOT NULL,
    gate_id VARCHAR(5) NOT NULL,
    CONSTRAINT fk_flight_dep_airport FOREIGN KEY(departure_airport_id) REFERENCES airport(airport_code),
    CONSTRAINT fk_flight_arr_airport FOREIGN KEY(arrival_airport_id) REFERENCES airport(airport_code),
    CONSTRAINT fk_flight_gate FOREIGN KEY(gate_id) REFERENCES gate(gate_id),
    CHECK(departure_time < arrival_time),
    CHECK(departure_airport_id != arrival_airport_id)
);

-- Ticket Table

CREATE TABLE ticket (
    ticket_id INT(13) PRIMARY KEY,
    passenger_id INT(10),
    flight_id INT(10),
    ticket_class CHAR(1) NOT NULL CHECK(ticket_class IN ('Y','B','F','W')),
    ticket_seat VARCHAR(4) NOT NULL,
    ticket_price DECIMAL(7,2) NOT NULL CHECK(ticket_price > 0),
    CONSTRAINT fk_ticket_passenger FOREIGN KEY(passenger_id) REFERENCES passenger(passenger_id),
    CONSTRAINT fk_ticket_flight FOREIGN KEY(flight_id) REFERENCES flight(flight_id)
);

-- Baggage Table

CREATE TABLE baggage (
    passenger_id INT(10) NOT NULL,
    sequence_num INT(2) NOT NULL,
    baggage_type VARCHAR(20) NOT NULL CHECK(baggage_type IN ('CARRY_ON','CHECKED','OVERSIZED')),
    weight DECIMAL(5,2) NOT NULL CHECK(weight > 0),
    PRIMARY KEY(passenger_id, sequence_num),
    CONSTRAINT fk_baggage_passenger FOREIGN KEY(passenger_id) REFERENCES passenger(passenger_id) ON DELETE CASCADE
);

-- Employee Phone Table

CREATE TABLE employee_phone (
    emp_id INT(7) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    PRIMARY KEY(emp_id, phone_number),
    CONSTRAINT fk_emp_id FOREIGN KEY(emp_id) REFERENCES employee(Emp_id)
);

-- Employee Assignment Table

CREATE TABLE employee_assignment (
    emp_id INT(7) NOT NULL,
    flight_id INT(10) NOT NULL,
    assignment_date DATE NOT NULL,
    PRIMARY KEY(emp_id, flight_id),
    CONSTRAINT fk_assignment_flight FOREIGN KEY(flight_id) REFERENCES flight(flight_id),
    CONSTRAINT fk_assignment_employee FOREIGN KEY(emp_id) REFERENCES employee(Emp_id)
);