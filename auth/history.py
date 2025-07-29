<!DOCTYPE html>
<html>
<head>
  <title>Lịch sử mua vé</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
  <div class="container mt-5 col-md-8">
    <div class="card shadow p-4">
      <h3 class="mb-4 text-center">Lịch sử mua vé</h3>
      <table class="table table-bordered table-hover">
        <thead class="table-secondary">
          <tr>
            <th>Mã đơn</th>
            <th>Phim</th>
            <th>Suất chiếu</th>
            <th>Ngày đặt</th>
            <th>Trạng thái</th>
            <th>Hành động</th>
          </tr>
        </thead>
        <tbody>
          {% for order in orders %}
          <tr>
            <td>{{ order.id }}</td>
            <td>{{ order.movie }}</td>
            <td>{{ order.showtime }}</td>
            <td>{{ order.date }}</td>
            <td>{{ order.status }}</td>
            <td>
              <a href="/order/{{ order.id }}" class="btn btn-info btn-sm">Xem chi tiết</a>
            </td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
</body>
</html> 
