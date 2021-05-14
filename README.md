# -xla
Sudoku AI

Vấn đề :
Bài toán sudoku kinh điển là 1 bài toán logic,  là một trò chơi câu đố sắp xếp chữ số dựa trên logic theo tổ hợp. Sudoku sẽ được cho sẵn một vài con số và nằm ở những vị trí bất kỳ.  Nhiệm vụ của người chơi là điền các chữ số vào một lưới 9×9 sao cho mỗi hàng, mỗi cột, và cả mỗi phần trong số chín lưới con 3×3 cấu tạo nên lưới chính đều chứa tất cả các chữ số từ 1 tới 9.
Vậy có thể áp dụng kĩ thuật xử lý ảnh để đưa ra kết quả một cách nhanh nhất khi có đầu vào là một bức ảnh hay không ?
Ý tưởng :
Đầu vào là 1 bức ảnh lưới 9*9 với các ô đã được điền số và các ô trống
 
Xóa lưới bằng cách xác định các đường biên ngang và dọc 
 



Cắt ảnh thành các cell nhỏ kích thước cố định
 
Detect số từ các cell nhỏ đó
 

Giải thật bằng backtracking 
Khó khăn :
1.	đầu vào là ảnh chụp nên không thể có đúng transform theo ttrujc xyz
hướng giải quyết : 
	 
                                              
Hướng giải quyết :
tìm 4 đỉnh là 4 góc của hình để transform ảnh đầu vào thành hình vuông
Tìm các biên là đường thẳng sau đó tìm góc quay của ảnh 

