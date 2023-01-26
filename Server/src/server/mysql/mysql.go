package mysql

import (
	"gorm.io/driver/mysql"
	"gorm.io/gorm"

	"fmt"
)

var (
	db *gorm.DB
)

func OpenDB() {
	fmt.Println("mysqldb->open db")
	dsn := "root:123456@tcp(localhost:3306)/poker?parseTime=true"
	db1, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})
	if err != nil {
		panic("connect db error")
	}
	db = db1
}

func MysqlDB() *gorm.DB {
	return db
}
