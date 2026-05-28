SELECT f.airline, AVG(t.ticket_price) AS average_ticket_price
FROM flight f
JOIN ticket t ON f.flight_id = t.flight_id
GROUP BY f.airline
ORDER BY average_ticket_price DESC;