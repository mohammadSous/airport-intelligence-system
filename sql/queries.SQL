SELECT 
    f.flight_id,
    f.airline,
    f.status,
    dep_airport.airport_name AS departure_airport,
    arr_airport.airport_name AS arrival_airport,
    f.departure_time,
    f.arrival_time,
    CONCAT('Terminal ', g.terminal, ' - Gate ', g.gate_number) AS gate_info
FROM flight f
    JOIN airport dep_airport ON f.departure_airport_id = dep_airport.airport_code
    JOIN airport arr_airport ON f.arrival_airport_id = arr_airport.airport_code
    JOIN gate g ON f.gate_id = g.gate_id
ORDER BY f.departure_time;

SELECT 
    f.airline,
    COUNT(t.ticket_id) AS total_tickets_sold,
    SUM(t.ticket_price) AS total_revenue,
    AVG(t.ticket_price) AS average_ticket_price,
    MIN(t.ticket_price) AS cheapest_ticket,
    MAX(t.ticket_price) AS most_expensive_ticket
FROM flight f
    JOIN ticket t ON f.flight_id = t.flight_id
GROUP BY f.airline
ORDER BY total_revenue DESC;


SELECT 
    p.passenger_id,
    CONCAT(p.p_first_name, ' ', COALESCE(p.p_middle_name, ''), ' ', p.p_last_name) AS full_name,
    p.passenger_nationality,
    f.flight_id,
    f.airline,
    f.destination,
    t.ticket_class,
    t.ticket_seat,
    COUNT(b.sequence_num) AS baggage_count,
    COALESCE(SUM(b.weight), 0) AS total_baggage_weight
FROM passenger p
    JOIN ticket t ON p.passenger_id = t.passenger_id
    JOIN flight f ON t.flight_id = f.flight_id
    LEFT JOIN baggage b ON p.passenger_id = b.passenger_id
GROUP BY p.passenger_id, p.p_first_name, p.p_middle_name, p.p_last_name, 
         p.passenger_nationality, f.flight_id, f.airline, f.destination, 
         t.ticket_class, t.ticket_seat
ORDER BY f.flight_id, t.ticket_seat;


SELECT 
    e.Emp_id,
    CONCAT(e.emp_first_name, ' ', e.emp_last_name) AS employee_name,
    e.emp_role,
    COUNT(ea.flight_id) AS flights_assigned,
    GROUP_CONCAT(DISTINCT f.airline ORDER BY f.airline) AS airlines_worked,
    MIN(ea.assignment_date) AS first_assignment,
    MAX(ea.assignment_date) AS latest_assignment
FROM employee e
    JOIN employee_assignment ea ON e.Emp_id = ea.emp_id
    JOIN flight f ON ea.flight_id = f.flight_id
WHERE ea.assignment_date >= '2025-05-01'
GROUP BY e.Emp_id, e.emp_first_name, e.emp_last_name, e.emp_role
HAVING COUNT(ea.flight_id) > 1
ORDER BY flights_assigned DESC;


SELECT 
    b.baggage_type,
    COUNT(*) AS total_pieces,
    SUM(b.weight) AS total_weight,
    AVG(b.weight) AS average_weight_per_piece,
    MIN(b.weight) AS lightest_bag,
    MAX(b.weight) AS heaviest_bag
FROM baggage b
    JOIN passenger p ON b.passenger_id = p.passenger_id
GROUP BY b.baggage_type
ORDER BY total_weight DESC;
