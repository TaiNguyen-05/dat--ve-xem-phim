<!DOCTYPE html>
<html>
<head>
  <title>Đặt vé xem phim</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
  <div class="container mt-5 col-md-8">
    <div class="card shadow p-4">
      <h3 class="mb-4 text-center">Đặt vé xem phim</h3>
      <form>
        <!-- Chọn phim -->
        <div class="mb-3">
          <label for="movie" class="form-label">Chọn phim</label>
          <select class="form-select" id="movie" name="movie">
            {% for movie in movies %}
              <option value="{{ movie }}">{{ movie }}</option>
            {% endfor %}
          </select>
        </div>
        <!-- Chọn suất chiếu -->
        <div class="mb-3">
          <label for="showtime" class="form-label">Chọn suất chiếu</label>
          <select class="form-select" id="showtime" name="showtime">
            {% for showtime in showtimes %}
              <option value="{{ showtime }}">{{ showtime }}</option>
            {% endfor %}
          </select>
        </div>
        <!-- Chọn khung giờ -->
        <div class="mb-3">
          <label for="time" class="form-label">Chọn khung giờ</label>
          <select class="form-select" id="time" name="time">
            {% for t in times %}
              <option value="{{ t }}">{{ t }}</option>
            {% endfor %}
          </select>
        </div>
        <!-- Chọn ghế -->
        <div class="mb-3">
          <label class="form-label">Chọn ghế</label>
          <div>
            {% for seat in seats %}
              <input type="checkbox" class="btn-check" id="seat{{ seat }}" name="seats" value="{{ seat }}" autocomplete="off">
              <label class="btn btn-outline-primary mb-1" for="seat{{ seat }}">{{ seat }}</label>
            {% endfor %}
          </div>
        </div>
        <!-- Chọn combo -->
        <div class="mb-3">
          <label class="form-label">Chọn combo</label>
          {% for combo in combos %}
            <div class="form-check">
              <input class="form-check-input" type="checkbox" value="{{ combo.id }}" id="combo{{ combo.id }}" name="combos">
              <label class="form-check-label" for="combo{{ combo.id }}">
                {{ combo.name }}
              </label>
            </div>
          {% endfor %}
        </div>
        <div class="text-center">
          <button type="submit" class="btn btn-success">Tiếp tục</button>
        </div>
      </form>
      <form action="/momo_payment" method="post">
        <input type="hidden" name="amount" value="10000">
        <div class="text-center">
          <button type="submit" class="btn btn-pink" style="background-color:#e83e8c;color:white;">Thanh toán MOMO</button>
        </div>
      </form>
    </div>
  </div>
</body>
</html> 
