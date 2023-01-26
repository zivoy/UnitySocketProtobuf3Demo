package main

import (
	"fmt"
	"github.com/name5566/leaf"
	lconf "github.com/name5566/leaf/conf"
	"unityDemoServer/src/server/conf"
	"unityDemoServer/src/server/game"
	"unityDemoServer/src/server/gamedata"
	"unityDemoServer/src/server/gate"
	"unityDemoServer/src/server/login"
	"unityDemoServer/src/server/mysql"
)

func main() {
	mysql.OpenDB()
	lconf.LogLevel = conf.Server.LogLevel
	lconf.LogPath = conf.Server.LogPath
	lconf.LogFlag = conf.LogFlag
	lconf.ConsolePort = conf.Server.ConsolePort
	lconf.ProfilePath = conf.Server.ProfilePath

	gamedata.LoadTables()
	testData := gamedata.GetTestTableByID(2)
	fmt.Println(testData.Name)

	leaf.Run(
		game.Module,
		gate.Module,
		login.Module,
	)

}

func InitDBTable() {

}
