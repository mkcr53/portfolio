# Portfolio

## Tableau sales data visualization 
This is where the description for this will go 
This links to a Public version of Tableau that shows charts of Profit Margins [Tableau Sales Viz](https://www.example.com)

## Rental DVD SQL

![DVD Rental Database Schema](https://github.com/mkcr53/portfolio/blob/main/dvd-rental-sample-database-diagram.png)

Ex Query: Which film was most rented in the United States?
```SQL
SELECT film.title, COUNT(rental.rental_id) AS rental_count
FROM rental
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film ON inventory.film_id = film.film_id
JOIN customer ON rental.customer_id = customer.customer_id
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
JOIN country ON city.country_id = country.country_id
WHERE country.country = 'United States'
GROUP BY film.title
ORDER BY rental_count DESC;
```
