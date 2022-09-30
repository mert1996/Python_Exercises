group_size = int(input())

room_number = list(map(int, input().split()))
set_room_number = set(room_number)

set_room_number = list(set_room_number)

print(set_room_number[len(set_room_number)-1])
