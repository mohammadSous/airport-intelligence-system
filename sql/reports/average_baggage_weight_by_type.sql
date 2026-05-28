SELECT
    baggage_type,
    COUNT(*) AS total_bags,
    AVG(weight) AS average_weight
FROM baggage
GROUP BY baggage_type
ORDER BY average_weight DESC;