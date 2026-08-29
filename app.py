import streamlit as st

# =========================
# CẤU HÌNH
# =========================

st.set_page_config(
    page_title="CV - Đặng Phú Hưng",
    page_icon="📄",
    layout="wide"
)

# =========================
# CSS
# =========================

st.markdown("""
<style>
.title {
    font-size: 36px;
    font-weight: bold;
    color: #17365D;
}

.subtitle {
    font-size: 18px;
    color: #555;
}

h2 {
    color: #17365D;
    border-bottom: 2px solid #17365D;
    padding-bottom: 5px;
}

.info {
    line-height: 1.8;
}
</style>
""", unsafe_allow_html=True)


# =========================
# THÔNG TIN CÁ NHÂN + ẢNH
# =========================

col1, col2 = st.columns([1, 3])

with col1:
    st.image("avatar.jpg", width=180)

with col2:

    st.markdown(
        '<div class="title">ĐẶNG PHÚ HƯNG</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">SINH VIÊN NĂM 3 NGÀNH TÀI CHÍNH NGÂN HÀNG</div>',
        unsafe_allow_html=True
    )

    st.write("")

    info1, info2 = st.columns(2)

    with info1:
        st.write("**Ngày sinh:** 05/07/2005")
        st.write("**Giới tính:** Nam")
        st.write("**Số điện thoại:** 0909116235")

    with info2:
        st.write("**Email:** phuhung5705@gmail.com")
        st.write("**Website:** Facebook")
        st.write("**Địa chỉ:** 80/21 Tô Vĩnh Diện, Khu phố Tân Hòa, Phường Đông Hòa, Thành phố Hồ Chí Minh")


# =========================
# MỤC TIÊU NGHỀ NGHIỆP
# =========================

st.markdown("## MỤC TIÊU NGHỀ NGHIỆP")

st.write("""
Áp dụng kiến thức chuyên ngành Tài chính – Ngân hàng cùng kỹ năng
Word, Excel và phân tích dữ liệu để hỗ trợ hiệu quả các nghiệp vụ ngân hàng.
Không ngừng học hỏi quy trình nghiệp vụ, nâng cao kỹ năng chuyên môn
và hướng tới trở thành nhân sự ngân hàng chuyên nghiệp,
có giá trị lâu dài cho tổ chức.
""")


# =========================
# CHIA 2 CỘT
# =========================

left, right = st.columns([1, 2])


# =========================
# CỘT TRÁI
# =========================

with left:

    # HỌC VẤN
    st.markdown("## HỌC VẤN")

    st.write("**19/2023 - nay**")
    st.write("**Trường Đại học Nguyễn Tất Thành**")
    st.write("Chuyên ngành: Tài chính ngân hàng")
    st.write("• Xếp loại: Khá")
    st.write("• Chứng chỉ: Kỹ năng Hành chính văn phòng")
    st.write("• Kỹ năng làm chủ công việc")


    # CHỨNG CHỈ
    st.markdown("## CHỨNG CHỈ")

    st.write("**2025**")
    st.write("Kỹ năng Hành chính văn phòng")

    st.write("**2025**")
    st.write("Kỹ năng làm chủ công việc")


    # KỸ NĂNG
    st.markdown("## KỸ NĂNG")

    st.write("**Soạn thảo văn bản**")
    st.write("""
    Kỹ năng soạn thảo văn bản hành chính và học thuật.
    Thành thạo Microsoft Word, trình bày văn bản chuyên nghiệp.
    Kỹ năng viết và chỉnh sửa báo cáo.
    """)

    st.write("**Kỹ năng bàn phím**")
    st.write("""
    Kỹ năng bàn phím tốt, gõ nhanh và chính xác,
    sử dụng thành thạo phím tắt trong Word và Excel.
    """)

    st.write("**Giải quyết vấn đề**")
    st.write("""
    Phân tích tình huống, xác định nguyên nhân,
    đề xuất và lựa chọn giải pháp phù hợp.
    """)

    st.write("**Quản lý thời gian**")
    st.write("""
    Sắp xếp công việc theo mức độ ưu tiên,
    đảm bảo hoàn thành đúng hạn, cân bằng học tập và công việc.
    """)


    # SỞ THÍCH
    st.markdown("## SỞ THÍCH")

    st.write("""
    • Đọc sách  
    • Nghe podcast học tập  
    • Tham gia hoạt động học thuật  
    • Tự học kỹ năng mềm
    """)


# =========================
# CỘT PHẢI
# =========================

with right:

    st.markdown("## HOẠT ĐỘNG")


    # HOẠT ĐỘNG 2024

    st.write("### 11/05/2024 - 23/12/2024")

    st.write("**TRƯỜNG ĐẠI HỌC NGUYỄN TẤT THÀNH**")

    st.write("**SINH VIÊN THAM GIA**")

    st.write("""
    • Tham gia UNITOUR nhà lãnh đạo tương lai và giới thiệu
    cuộc thi ASEAN - CHINA - INDIA 2024.

    • Tham gia Ngày hội tuyển dụng tháng 5 năm 2024.

    • Tham gia Workshop Đầu tư chứng khoán
    "Bản lĩnh đầu tư & tự tin chiến thắng".

    • Tham gia Chương trình Tìm hiểu tài nguyên giáo dục mở
    cho Tân SV khóa 2024.
    """)


    # HOẠT ĐỘNG 2025

    st.write("### 09/08/2025 - 05/10/2025")

    st.write("**TRƯỜNG ĐẠI HỌC NGUYỄN TẤT THÀNH**")

    st.write("**SINH VIÊN THAM GIA**")

    st.write("""
    • Tham gia Hội thảo khoa học Quốc tế
    Toán học và Ứng dụng năm 2025.

    • Tham gia Hoạt động phục vụ cộng đồng cấp Khoa 2025 -
    Hành trình tuổi trẻ vì cộng đồng 2025 -
    Trung thu nghĩa tình 2025.
    """)


# =========================
# CUỐI CV
# =========================

st.divider()

st.caption("CV - Đặng Phú Hưng")
