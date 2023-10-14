from view.divider import divider

#  =============================================
#         Aplikasi Penggajian Karyawan
#                  PT.Casya
#  =============================================
def welcome_txt():
    welcome_text = "Aplikasi Penggajian Karyawan"
    pt_text = "PT.Casya"
    divider("=")

    # Menghitung panjang teks dan lebar garis pembatas
    welcome_length = len(welcome_text)
    pt_length = len(pt_text)
    divider_width = 45  # Lebar garis pembatas

  
    welcome_left_padding = (divider_width - welcome_length) // 2
    welcome_right_padding = divider_width - welcome_length - welcome_left_padding

   
    pt_left_padding = (divider_width - pt_length) // 2
    pt_right_padding = divider_width - pt_length - pt_left_padding

    # Mencetak teks aplikasi dengan spasi di sekitarnya
    print(" " * welcome_left_padding + welcome_text + " " * welcome_right_padding)

    # Mencetak teks PT dengan spasi di sekitarnya
    print(" " * pt_left_padding + pt_text + " " * pt_right_padding)

    divider("=")