<div align="center">

# Sudoku Solver

</div>

<div style="display: flex; align-items: center;">
  <img src="image/logoSudoku.png" alt="Sudoku Example" width="25" style="margin-right: 8px;">
  <h2>Giới thiệu về sudoku</h2>
</div>

- Sudoku là một trò chơi giải đố nổi tiếng, với người chơi phải điền các số từ 1 đến 9 vào bảng 9x9 sao cho một số ở mỗi hàng, mỗi cột và mỗi khối 3x3 chỉ xuất hiện một lần duy nhất.
- Khởi đầu của ván sudoku là một bảng 9x9 được chia làm 9 khối, và người chơi sẽ được cung cấp một vài manh mối ngay khi trò chơi bắt đầu. Nhiệm vụ của người chơi là phải hoàn thành tất cả các ô trống còn lại sao cho thỏa mãn luật chơi.
- Nguồn gốc của trò chơi này là từ câu đố "Number Place" của Mỹ, nhưng được công ty Nikoli của Nhật Bản đặt tên và phổ biến rộng rãi trên toàn thế giới và đầu những năm 2000.

<p align="center">
  <img src="image/gioiThieu.png" alt="Sudoku Example" width="300">
</p>

<hr>

<div style="display: flex; align-items: center;">
  <img src="image/logoThuatToan.jpeg" alt="Sudoku Example" width="40" style="margin-right: 8px;">
  <h2>Thuật toán giải Sudoku</h2>
</div>


<p style="font-size:18px"><b>Sử dụng thuật toán Backtracking (quay lui)</b></p>

- Thuật toán Backtracking được thiết kế dựa trên đệ quy (recursion) được đề ra đầu tiên bởi nhà toán học người Mỹ Derrick Henry "Dick" Lehmer vào những năm 1950. 
- Bản chất của Backtracking là thuật toán tìm kiếm theo chiều sâu (Depth-first search)
<h3>Ý tưởng</h3>
- Dùng để giải bài toán liệt kê các cấu hình. Mỗi cấu hình được xây dựng bằng từng phần tử. Mỗi phần tử lại được chọn bằng cách thử tất cả các khả năng.
<h3>Các bước trong liệt kê cấu hình dạng X[1..n]</h3>
- Xét tất cả các giá trị X[1] có thể nhận, thử X[1] nhận các giá trị đó. Với mỗi giá trị của X[1] ta sẽ:
- Xét tất cả các giá trị X[2] có thể nhận, thử X[2] cho các giá trị đó. Với mỗi giá trị X[2] lại xét các giá trị của X[3] và tiếp tục như vậy cho đến:
- Xét tất cả các giá trị X[n] có thể nhận, thử cho X[n] nhận lần lượt giá trị đó.
- Thông báo cấu hình tìm được.
<p align="center">
  <img src="image/minhHoaBacktracking.png" alt="Sudoku Example" width="300">
</p>
 <p style="font-size:18px"><b>Mã giả của thuật toán</b></p>
<p align="center">
  <img src="image/maGiaThuatToan.png" alt="Sudoku Example" width="300">
</p>
<hr>

<h2>Nguồn tham khảo</h2>
https://en.wikipedia.org/wiki/Sudoku_solving_algorithms <br>
https://www.thegioididong.com/game-app/huong-dan-cach-choi-game-o-so-sudoku-chien-thuat-luat-choi-co-1320525 <br>
https://vncoder.vn/bai-viet/tim-hieu-ve-thuat-toan-quay-lui-backtracking-qua-tro-choi-sudoku <br>
