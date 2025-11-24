# 🖥️ CẨM NANG TỐI ƯU MÀN HÌNH LG 27UP600 (4K IPS)

Tài liệu này tổng hợp các thông số cài đặt chuẩn nhất để khắc phục tình trạng sai màu hoặc mỏi mắt trên màn hình LG 27UP600, giúp tận dụng tối đa tấm nền 4K IPS.

---

## 📑 MỤC LỤC

1. [Chuẩn Bị Đầu Vào (Quan Trọng Nhất)](#1-chuẩn-bị-đầu-vào-pcwindows---quan-trọng)
2. [Profile Tối Ưu: Làm Việc & Lướt Web](#2-profile-tối-ưu-làm-việc--lướt-web-chuẩn-srgb)
3. [Profile Tối Ưu: Xem Phim & Game (SDR)](#3-profile-tối-ưu-xem-phim--game-offline-sdr)
4. [Chế Độ HDR (4K Cinema)](#4-chế-độ-hdr-tự-động-kích-hoạt)
5. [Giải Mã Các Chế Độ Có Sẵn](#5-giải-mã-các-chế-độ-có-sẵn-của-nhà-sản-xuất)
6. [Mẹo Tự Động Hóa (Pro Tip)](#6-mẹo-chuyên-nghiệp-tự-động-hóa-profile)

---

## 1. Chuẩn Bị Đầu Vào (PC/Windows) - QUAN TRỌNG
*Làm bước này trước khi chỉnh nút trên màn hình để tránh màu đen bị xám xịt.*

1.  **Tắt "Tiết kiệm năng lượng" trên màn hình:**
    * Menu OSD → `General` → `Smart Energy Saving` → Chọn **Off**.
    * *(Ngăn màn hình tự động tối đi gây khó chịu).*
2.  **Cài đặt dải màu trên Windows:**
    * Mở **Nvidia Control Panel** (hoặc AMD Software).
    * Vào mục `Display` → `Change resolution`.
    * Kéo xuống phần **Output color settings**:
        * **Output color depth:** Chọn **10 bpc** (nếu có) hoặc 8 bpc.
        * **Output dynamic range:** Chọn **Full** (Tuyệt đối không để *Limited*).

---

## 2. Profile Tối Ưu: Làm Việc & Lướt Web (Chuẩn sRGB)
**Mục tiêu:** Màu sắc trung thực, dịu mắt, chữ sắc nét không bị gai/viền trắng.

* **Picture Mode:** Chọn **Custom** (Tùy chỉnh).

### ⚙️ Bảng Thông Số Chi Tiết

| Hạng mục | Cài đặt | Giải thích tác dụng |
| :--- | :--- | :--- |
| **Brightness** | **20 - 35** | Mức sáng an toàn cho mắt khi ngồi gần và làm việc lâu. |
| **Contrast** | **70** | Mức tiêu chuẩn (Mặc định). Không tăng cao hơn để giữ chi tiết. |
| **Sharpness** | **50** | Mức trung tính. |
| **Super Resolution+** | **OFF (Tắt)** | ⚠️ **Quan trọng:** Phải TẮT để chữ không bị viền trắng/gai. |
| **Black Level** | **High** | Hiển thị đầy đủ dải màu đen (khi PC để Full Range). |
| **DFC** | **Off** | Tắt tương phản động. |

### 🎨 Cài đặt Nâng cao (Game/Color Adjust)
* **Response Time:** **Fast** (Tránh chọn *Faster* để không bị lỗi bóng ma/inverse ghosting khi cuộn web).
* **Black Stabilizer:** **50** (Giữ nguyên).
* **Gamma:** **Mode 2** (Tương đương Gamma 2.2 - Chuẩn thiết kế/Web).
* **Color Temp:** **Custom** (Red: **50** / Green: **50** / Blue: **50**).

---

## 3. Profile Tối Ưu: Xem Phim & Game Offline (SDR)
**Mục tiêu:** Hình ảnh rực rỡ, độ tương phản cao, màu đen sâu hơn (Cinematic look).

* **Picture Mode:** Chọn **Custom** (Hoặc *Cinema*).

### ⚙️ Bảng Thông Số Chi Tiết

| Hạng mục | Cài đặt | Giải thích tác dụng |
| :--- | :--- | :--- |
| **Brightness** | **60 - 100** | Tăng độ sáng để hình ảnh sống động, nổi bật. |
| **Contrast** | **70** | Giữ nguyên. |
| **Sharpness** | **50 - 60** | Có thể tăng nhẹ nếu nguồn phim mờ (Youtube 1080p). |
| **Super Resolution+** | **Low / Off** | Bật *Low* nếu cần tăng độ nét giả lập, *Off* nếu xem 4K Native. |

### 🎨 Cài đặt Nâng cao (Quan trọng)
* **Gamma:** **Mode 4**
    * *Lý do:* Mode 4 có đường cong gamma tối hơn, giúp màu đen trông sâu và đầm hơn, tạo độ nổi khối tốt cho phim ảnh.

---

## 4. Chế Độ HDR (Tự động kích hoạt)
*Lưu ý: Khi xem nội dung HDR, màn hình sẽ tự khóa cài đặt và hiện logo HDR ở góc.*

* **Picture Mode:**
    * ✅ **Khuyên dùng:** **HDR Standard** (Cân bằng) hoặc **HDR Cinema** (Ấm áp).
    * ❌ **Tránh xa:** **HDR Vivid** (Màu quá rực, bết màu, sai lệch tông da).
* **Brightness:** Màn hình tự khóa ở mức **100** (Max) để đạt độ sáng đỉnh ~400 nits.

---

## 5. Giải Mã Các Chế Độ Có Sẵn Của Nhà Sản Xuất

| Chế độ | Đánh giá | Khi nào nên dùng? |
| :--- | :--- | :--- |
| **Vivid** | ❌ Tệ | Chỉ dùng trưng bày siêu thị. Quá rực, sai màu, rất hại mắt. |
| **HDR Effect** | ❌ Tệ | Giả lập HDR làm da người bị đỏ, tương phản gắt. Không nên dùng. |
| **Reader** | ✅ Tốt (Đêm) | Lọc ánh sáng xanh (ám vàng). Chỉ dùng đọc văn bản ban đêm. |
| **sRGB** | ⚠️ Khá | Giới hạn màu chuẩn in ấn. Nhược điểm là thường bị khóa độ sáng cố định. |

---

## 6. Mẹo Chuyên Nghiệp: Tự Động Hóa Profile 💡

Thay vì thò tay ra sau màn hình bấm nút Joystick mỗi lần chuyển việc, hãy cài phần mềm chính chủ **LG OnScreen Control**.

**Tính năng "My Application Presets":**
1.  Gán ứng dụng **Excel / Chrome / Word** ➔ Tự động chuyển màn hình về profile **Custom (Làm việc)**.
2.  Gán ứng dụng **MPV Player / Netflix / Game** ➔ Tự động chuyển màn hình về profile **Cinema (Giải trí)**.

> **Ghi chú:** LG 27UP600 là màn hình IPS, khi xem phim trong phòng tối hoàn toàn sẽ thấy hở sáng ở góc (IPS Glow). Để khắc phục, nên bật một đèn ngủ nhẹ phía sau màn hình (Bias Lighting) để đánh lừa thị giác, giúp màu đen trông sâu hơn.
