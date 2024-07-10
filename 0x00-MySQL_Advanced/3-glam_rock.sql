-- Create a tmp file to compute lifespan

SELECT band_name AS band_name, IFNULL(split, 2020) - IFNULL(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%';

-- Rank the bands by longevity
ORDER BY lifespan DESC;
