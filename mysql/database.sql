use mydatabase;

-- create admin table
CREATE TABLE admin(  
					id INT NOT NULL AUTO_INCREMENT,
					name VARCHAR(255),
                    address VARCHAR(255),
                    age INT NOT NULL,
                    PRIMARY KEY (id)
                    );

