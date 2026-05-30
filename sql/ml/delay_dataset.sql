SELECT
    f.airline,
    f.origin,
    f.destination,
    f.gate_id,

    HOUR(f.departure_time) AS departure_hour,
    DAYOFWEEK(f.departure_time) AS departure_day_of_week,

    COUNT(DISTINCT t.ticket_id) AS tickets_sold,
    COALESCE(AVG(t.ticket_price), 0) AS average_ticket_price,

    COUNT(DISTINCT ea.emp_id) AS employee_count,

    COUNT(DISTINCT CONCAT(b.passenger_id, '-', b.sequence_num)) AS baggage_count,
    COALESCE(SUM(b.weight), 0) AS total_baggage_weight,

    CASE
        WHEN f.status = 'DELAYED' THEN 1
        ELSE 0
    END AS is_delayed

FROM flight f

LEFT JOIN ticket t
    ON f.flight_id = t.flight_id

LEFT JOIN baggage b
    ON t.passenger_id = b.passenger_id

LEFT JOIN employee_assignment ea
    ON f.flight_id = ea.flight_id

GROUP BY
    f.flight_id,
    f.airline,
    f.origin,
    f.destination,
    f.gate_id,
    f.departure_time,
    f.status

ORDER BY f.flight_id;