# 🎧 MPV Audio Tips & Optimization Collection

> **Tổng hợp các cấu hình, script và hướng dẫn tối ưu hóa âm thanh chuyên sâu cho MPV Player.**
> *Dành cho hệ thống: DAC rời (F.Audio/Topping...), Loa 2.0/2.1, Tai nghe High-End.*

[![MPV](https://img.shields.io/badge/MPV-0.36%2B-blueviolet?style=flat-square&logo=mpv)](https://mpv.io/)
[![Audio](https://img.shields.io/badge/Audio-Audiophile-orange?style=flat-square&logo=audacity)](https://github.com/blamag999/audio-tips)
[![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)]()

---

## 📑 Mục Lục (Table of Contents)

### 📂 1. Cấu Hình Cốt Lõi (Core Configs)
Các file cấu hình `mpv.conf` được tinh chỉnh cho từng mục đích nghe.

| File Name | Mô tả chức năng |
| :--- | :--- |
| [**`mpv_audiophile.conf`**](./mpv_audiophile.conf) | 💎 **Chất lượng cao nhất.** WASAPI Exclusive, SOXR Resampler, Dither. Dành cho nghe nhạc Lossless. |
| [**`mpv_movies.conf`**](./mpv_movies.conf) | 🎬 **Tối ưu phim ảnh.** Auto Downmix 5.1/7.1 về Stereo/2.1. Giữ lực Bass cho Subwoofer. |
| [**`mpv_nightmode.conf`**](./mpv_nightmode.conf) | 🌙 **Chế độ ban đêm.** Tích hợp Compressor nén dải động, tăng lời thoại, giảm tiếng nổ. |

### 🎛️ 2. Profiles Âm Thanh (Advanced Profiles)
Đoạn mã dùng trong `profiles.conf` để tự động kích hoạt theo điều kiện.

| Profile Name | Tác dụng | Trigger (Kích hoạt) |
| :--- | :--- | :--- |
| `[Audio_Downmix_2.1]` | Trộn kênh LFE (Bass) và Center (Thoại) vào 2 loa chính. | Tự động khi nguồn là 5.1/7.1 |
| `[Audio_Night_Mode]` | Cân bằng âm lượng động (Dynamic Normalization). | Kích hoạt bằng phím tắt |
| `[Audio_Pure_Direct]` | Bỏ qua mọi bộ lọc (No filters), xuất nguyên bản. | Dành cho nhạc Stereo 2.0 |

### ⌨️ 3. Phím Tắt (Keybindings)
Các thiết lập cho `input.conf`.

- [**`input_audio.conf`**](./input_audio.conf) - Tổng hợp phím tắt điều khiển Audio:
    - `n`: Bật/Tắt Night Mode.
    - `Shift+n`: Chuyển đổi Downmix (2.0 vs 2.1).
    - `Ctrl+a`: Reload lại driver âm thanh (Fix lỗi mất tiếng).

---

## 📖 Hướng Dẫn Chi Tiết (Guides)

### 🛠️ Tối ưu phần cứng (Hardware Setup)
1.  **[DAC_Setup_Guide.md](./docs/DAC_Setup_Guide.md)**
    - Cách thiết lập Windows ở chế độ 32-bit/384kHz.
    - Tại sao nên để Volume Windows 100%?
2.  **[Subwoofer_Crossover.md](./docs/Subwoofer_Crossover.md)**
    - Cách cắt tần số (Crossover) trên Sub điện (Polk, Yamaha...).
    - Chỉnh Phase sao cho đồng bộ với loa chính.

### 🎚️ Thủ thuật phần mềm (Software Tricks)
* **Cách khử tiếng vang (Reverb)** cho phòng chưa tiêu âm.
* **Sửa lỗi lệch tiếng (Audio Sync/Latency)** khi dùng loa Bluetooth.
* **Upscale âm thanh:** Biến nhạc MP3 128kbps nghe "đỡ tệ" hơn.

---

## 🚀 Cách Sử Dụng Nhanh

**Bước 1:** Tải file config bạn cần (ví dụ `mpv_audiophile.conf`).
**Bước 2:** Copy nội dung vào file `mpv.conf` gốc của bạn hoặc dùng lệnh `include`.

```ini
# Ví dụ trong mpv.conf của bạn:
include="~~/audio-tips/mpv_audiophile.conf"
