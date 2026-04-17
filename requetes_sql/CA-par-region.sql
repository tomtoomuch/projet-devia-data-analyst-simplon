-- CA par région --
SELECT SUM(prix * qte)
FROM ventes
GROUP BY region
ORDER BY region