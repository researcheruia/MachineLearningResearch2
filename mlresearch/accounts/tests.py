from django.test import TestCase


from .models import CustomUser


class CustomUserTest(TestCase):
    def test_create_user(self):
        User = CustomUser
        user = User.objects.create_user(
            username="mvmoras271091",
            first_name="Marcus",
            last_name="Mora",
            email="mvmoras@edu.uia.ac.cr",
            password="KLrLiLsLtLeL_Ez_MuY.B0_N_1_TA",
            birth_date="1991-10-27",
        )
        self.assertEqual(user.username, "mvmoras271091")
        self.assertEqual(user.first_name, "Marcus")
        self.assertEqual(user.last_name, "Mora")
        self.assertEqual(user.email, "mvmoras@edu.uia.ac.cr")
        self.assertEqual(user.birth_date, "1991-10-27")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = CustomUser
        admin_user = User.objects.create_superuser(
            username="JuanJuan",
            email="mvmoras@outlook.com",
            password="IOP.64p",
            birth_date="1991-10-27",
        )
        self.assertEqual(admin_user.username, "JuanJuan")
        self.assertEqual(admin_user.email, "mvmoras@outlook.com")
        self.assertEqual(admin_user.birth_date, "1991-10-27")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


