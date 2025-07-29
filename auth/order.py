<!DOCTYPE html>
<html>
<head>
  <title>Chi tiết đơn hàng</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
  <div class="container mt-5 col-md-6">
    <div class="card shadow p-4">
      <h3 class="mb-4 text-center">Chi tiết đơn hàng</h3>
      <ul class="list-group mb-3">
        <li class="list-group-item"><strong>Mã đơn:</strong> {{ order.id }}</li>
        <li class="list-group-item"><strong>Phim:</strong> {{ order.movie }}</li>
        <li class="list-group-item"><strong>Suất chiếu:</strong> {{ order.showtime }}</li>
        <li class="list-group-item"><strong>Khung giờ:</strong> {{ order.time }}</li>
        <li class="list-group-item"><strong>Ghế:</strong> {{ order.seats|join(', ') }}</li>
        <li class="list-group-item"><strong>Combo:</strong> {{ order.combos|join(', ') }}</li>
        <li class="list-group-item"><strong>Ngày đặt:</strong> {{ order.date }}</li>
        <li class="list-group-item"><strong>Trạng thái:</strong> {{ order.status }}</li>
        <li class="list-group-item"><strong>Tổng tiền:</strong> {{ order.total }} VNĐ</li>
      </ul>
      <div class="text-center">
        <a href="/history" class="btn btn-secondary">Quay lại lịch sử</a>
      </div>
    </div>
  </div>
</body>
</html> 
