SELECT
    status,
    COUNT(*) AS flight_count
FROM flight
GROUP BY status
ORDER BY flight_count DESC;