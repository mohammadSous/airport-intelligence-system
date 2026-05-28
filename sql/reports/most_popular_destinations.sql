SELECT 
    destination,
    COUNT(*) AS total_flights
FROM flight
GROUP BY destination
ORDER BY total_flights DESC;