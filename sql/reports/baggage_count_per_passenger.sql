SELECT 
    p.passenger_id,
    p.p_first_name,
    p.p_middle_name,
    p.p_last_name,
    COUNT(b.sequence_num) AS baggage_count
FROM passenger p
LEFT JOIN baggage b 
    ON p.passenger_id = b.passenger_id
GROUP BY 
    p.passenger_id,
    p.p_first_name,
    p.p_middle_name,
    p.p_last_name
ORDER BY baggage_count DESC;