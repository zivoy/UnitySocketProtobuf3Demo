protoc --proto_path=./Proto/src  --csharp_out=../Client/Assets/Scripts/Net/proto ./Proto/src/*.proto
protoc --proto_path=./Proto/src --go_out=../Server ./Proto/src/*.proto

python gen_proto.py