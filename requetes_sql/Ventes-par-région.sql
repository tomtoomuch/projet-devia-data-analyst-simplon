-- Quantité vendue par région --
SELECT SUM(qte)
FROM ventes
GROUP BY region
ORDER BY region