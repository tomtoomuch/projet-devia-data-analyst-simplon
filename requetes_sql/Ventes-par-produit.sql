-- Quantité vendue par produit --
SELECT SUM(qte)
FROM ventes
GROUP BY produit
ORDER BY produit