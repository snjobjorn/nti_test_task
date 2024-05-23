SELECT
    fact.user_ID,
    fact.fact_title,
    source.source_title,
    fact_detail.key AS detail_key,
    fact_detail.value AS detail_value,
    COUNT(fact.fact_ID) AS fact_count,
    COUNT(DISTINCT fact_detail.fact_detail_ID) AS detail_count
FROM
    fact
    LEFT JOIN source ON source.source_id = fact.source_ID
    LEFT JOIN fact_detail ON fact_detail.fact_id = fact.fact_ID
WHERE
    fact.is_deleted = 0
GROUP BY
    fact.user_ID
ORDER BY
    fact.ts DESC