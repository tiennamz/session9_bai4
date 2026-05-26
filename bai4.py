order_list = [    "GE001 - PENDING",   "GE002 - DELIVERING",    "GE003 - CANCELLED"]

menu = '''
===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====
1. Hiển thị danh sách đơn hàng
2. Cập nhật danh sách đơn hàng
3. Thống kê đơn hàng theo trạng thái
4. Thoát chương trình
'''
while True:
    print(menu)
    choice = input("Nhập lựa chọn của bạn: ")
    if choice.isdigit():
        choice = int(choice)
    else:
        print("Lựa chọn không hợp lệ")
        continue

    match choice:
        case 1: 
            if order_list == []:
                print(" Danh sách đơn hàng hiện đang trống.")
            else:
                print("Danh sách đơn hàng hiện tại:")
                for index, values in enumerate(order_list, start=1):
                    print(f"{index}. {values}")
        
        case 2:
            while True: 
                print('''
----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----
1. Thêm đơn hàng mới
2. Sửa đơn hàng theo vị trí
3. Xóa đơn hàng theo vị trí
4. Quay lại menu chính''')
                choice_child = input("Nhập lựa chọn của bạn: ")
                if choice_child.isdigit():
                    choice_child = int(choice_child)
                else:
                    print("Lựa chọn không hợp lệ")
                    continue
                
                if choice_child == 1:
                    id = input("Nhập mã sản phẩm: ").strip().upper()
                    status = input("Nhập trạng thái sản phẩm: ").strip().upper()
                    
                    order_list.append(id + " - " + status)
                    
                    print(order_list)
                
                elif choice_child == 2:
                    input_search = input("Nhập vị trí bạn muốn sửa: ")
                    if not input_search.isdigit() or int(input_search) > len(order_list):
                        print("Vị trí không hợp lệ!")
                    else:
                        input_search = int(input_search)
                        order_list[input_search - 1] = input("Nhập mã mới bạn muốn sửa ")
                        
                elif choice_child == 3:
                    input_search = input("Nhập vị trí bạn muốn xóa: ")
                    if not input_search.isdigit() or int(input_search) > len(order_list):
                        print("Vị trí không hợp lệ!")
                    else:
                        input_search = int(input_search)
                        order_list.pop(input_search - 1)    
                        print(order_list)                
                        
                elif choice_child == 4:
                    break
                else:
                    print("Không hợp lệ!!!!!") 
                    
        case 3:
            count_pending = 0
            count_delivering = 0
            count_cancelled = 0
            count_completed = 0
            for order in order_list:
                if order.find("PENDING") != -1:
                    count_pending += 1
                elif order.find("DELIVERING") != -1:
                    count_delivering += 1                       
                elif order.find("CANCELLED") != -1:
                    count_cancelled += 1                       
                elif order.find("COMPLETED") != -1:
                    count_completed += 1      
                    
            if order_list == []:
                print("""
===== THỐNG KÊ ĐƠN HÀNG =====
PENDING: 0
DELIVERING: 0
COMPLETED: 0
CANCELLED: 0
Tổng số đơn hàng: 0
                      """)  
            else:               
                print(f'''
===== THỐNG KÊ ĐƠN HÀNG =====
PENDING: {count_pending}
DELIVERING: {count_delivering}
COMPLETED: {count_completed}
CANCELLED: {count_cancelled}
Tổng số đơn hàng: {len(order_list)}                  
                    ''')
        
        case 4:
            print("Thoát chương trình")
            break
        
        case _: 
            print("Không hợp lệ")