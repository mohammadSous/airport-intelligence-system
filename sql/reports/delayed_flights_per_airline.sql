SELECT airline, COUNT(*) AS delayed_flights
FROM flight
WHERE status = 'DELAYED'
GROUP BY airline
ORDER BY delayed_flights DESC;