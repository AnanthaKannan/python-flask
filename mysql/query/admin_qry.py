get_all_admin = "select * from admin"
get_admin_by_name = "select * from admin where name = %s"
add_new_admin = "INSERT INTO admin (name, address, age) VALUES (%s, %s, %s)"
delete_admin_by_name = "DELETE FROM admin WHERE name = %s"