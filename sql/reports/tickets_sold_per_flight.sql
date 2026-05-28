SELECT 
    f.flight_id,
    f.airline,
    COUNT(t.ticket_id) AS tickets_sold
FROM flight f
JOIN ticket t 
    ON f.flight_id = t.flight_id
GROUP BY f.flight_id, f.airline
ORDER BY tickets_sold DESC;