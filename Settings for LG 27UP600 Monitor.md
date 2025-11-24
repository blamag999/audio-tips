# Hướng Dẫn Tối Ưu Cài Đặt LG 27UP600 (4K IPS)

Tài liệu này tổng hợp các thông số cài đặt tối ưu cho màn hình LG 27UP600 dựa trên hai mục đích sử dụng chính: **Làm việc/Lướt web** và **Giải trí/Xem phim**.

---

## 1. Cài Đặt Đầu Vào (PC/Windows) - QUAN TRỌNG

Trước khi chỉnh nút trên màn hình, hãy đảm bảo tín hiệu từ Card đồ họa xuất ra là đầy đủ nhất để tránh màu đen bị xám xịt.

* **Công cụ:** Nvidia Control Panel (hoặc AMD Radeon Software).
* **Đường dẫn:** `Display` -> `Change resolution`.
* **Cài đặt:** Tại mục *Output color format*:
    * **Output color depth:** 10 bpc (nếu có) hoặc 8 bpc.
    * **Output dynamic range:** **Full** (Tuyệt đối không để Limited).

---

## 2. Profile 1: Làm Việc & Lướt Web (Productivity)

**Mục tiêu:** Màu sắc trung thực (chuẩn sRGB), độ sáng thấp để bảo vệ mắt, chữ hiển thị sắc nét không bị gai.

### Picture Mode: **Custom (Tùy chỉnh)**

| Mục Cài Đặt | Thông số | Tác dụng |
| :--- | :--- | :--- |
| **Brightness** | **20 - 35** | Mức sáng an toàn cho mắt khi ngồi gần và làm việc lâu. |
| **Contrast** | **70** | Mức tiêu chuẩn, giữ chi tiết vùng sáng tốt nhất. |
| **Sharpness** | **50** | Mức trung tính. Không tăng cao hơn để tránh vỡ font chữ. |
| **Super Resolution+** | **OFF** | **Quan trọng:** Phải TẮT để chữ không bị viền trắng/gai. |
| **Black Stabilizer** | **50** | Giữ nguyên để màu đen đúng chuẩn. |
| **Response Time** | **Fast** | Tránh chọn *Faster* để không bị lỗi bóng ma (inverse ghosting) khi cuộn web. |

### Color Adjust
* **Gamma:** **Mode 2** (Tương đương Gamma 2.2 chuẩn đồ họa).
* **Color Temp:** **Custom** (Red: 50 / Green: 50 / Blue: 50).

---

## 3. Profile 2: Xem Phim & Giải Trí (Entertainment)

### A. Phim SDR (Youtube thường, Phim không HDR)
**Mục tiêu:** Hình ảnh rực rỡ, độ tương phản cao, tận dụng dải màu rộng DCI-P3.

| Mục Cài Đặt | Thông số | Tác dụng |
| :--- | :--- | :--- |
| **Picture Mode** | **Custom** | Hoặc chế độ "Cinema". |
| **Brightness** | **70 - 100** | Tăng độ sáng để hình ảnh sống động. |
| **Contrast** | **70** | Giữ nguyên. |
| **Sharpness** | **50 - 60** | Có thể tăng nhẹ lên 60 nếu xem video 1080p bị mờ. |
| **Super Resolution+** | **Low / Off** | Bật mức Low nếu nguồn phim mờ, nếu phim 4K thì nên Tắt. |
| **Gamma** | **Mode 4** | Gamma tối hơn, giúp màu đen sâu hơn, tăng độ nổi khối (chiều sâu). |

### B. Phim HDR (Phim 4K HDR, Youtube HDR)
**Lưu ý:** Khi bật phim HDR (và Windows đã bật HDR), màn hình sẽ tự chuyển sang chế độ HDR và khóa nhiều cài đặt.

* **Picture Mode:** Chọn **HDR Standard** (Chuẩn nhất) hoặc **HDR Cinema** (Ấm áp).
    * *Tránh:* HDR Vivid (Màu quá rực, sai lệch tông da).
* **Brightness:** Màn hình tự khóa ở **100** (Max) để kích hoạt độ sáng đỉnh ~400 nits.

---

## 4. Mẹo Chuyển Đổi Nhanh (Software)

Thay vì bấm nút cứng (joystick) trên màn hình, hãy cài đặt phần mềm **LG OnScreen Control** trên Windows.

* **Tự động hóa:** Bạn có thể gán Profile cho từng ứng dụng:
    * Mở **Excel / Chrome** -> Màn hình tự nhảy về Profile làm việc (Độ sáng thấp).
    * Mở **MPV / Netflix** -> Màn hình tự nhảy về Profile Cinema (Độ sáng cao).

> **Ghi chú:** LG 27UP600 là màn hình IPS, khi xem phim trong phòng tối hoàn toàn sẽ thấy hở sáng ở góc (IPS Glow). Để khắc phục, nên bật một đèn ngủ nhẹ phía sau màn hình (Bias Lighting) để đánh lừa thị giác, giúp màu đen trông sâu hơn.
