# Input: Số lượng phòng học cần kiểm tra, số hàng ghế của từng phòng, số ghế trên mỗi hàng
# Output: Sơ đồ chỗ ngồi của từng phòng

room_count = int(input("Nhập số lượng phòng học cần kiểm tra: "))
if room_count <= 0:
    print("Số lượng phòng học không hợp lệ")
    print("Chương trình kết thúc")
else:
    for room in range(1, room_count + 1):
        print(f"Phòng học {room}:")
        rows = int(input("Nhập số hàng ghế: "))
        cols = int(input("Nhập số ghế trên mỗi hàng: "))

        if rows <= 0 or cols <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue

        if rows > 10 or cols > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break

        for i in range(rows):
            for j in range(cols):
                print("*", end=" ")
            print()