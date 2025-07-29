<!DOCTYPE html>
<html>
<head>
  <title>Thanh toán MOMO</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
  <div class="container mt-5 col-md-6">
    <div class="card shadow p-4">
      <h3 class="mb-4 text-center">Thanh toán MOMO</h3>
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
