-- Buy buy buy
-- Creates a trigger that decreases the quantity of an item after add an order
CREATE TRIGGER order_decrease BEFORE INSERT ON orders
FOR EACH ROW UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
