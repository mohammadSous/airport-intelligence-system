SELECT airline, COUNT(*) AS total_flights
FROM flight
GROUP BY airline
ORDER BY total_flights DESC;