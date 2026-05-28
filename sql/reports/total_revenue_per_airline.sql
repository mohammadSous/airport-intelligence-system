SELECT 
    f.airline,
    SUM(t.ticket_price) AS total_revenue
FROM flight f
JOIN ticket t 
    ON f.flight_id = t.flight_id
GROUP BY f.airline
ORDER BY total_revenue DESC;