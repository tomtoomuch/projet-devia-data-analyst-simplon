-- Ventes par produits --
SELECT SUM(prix * qte)
FROM ventes
GROUP BY produit
ORDER BY produit