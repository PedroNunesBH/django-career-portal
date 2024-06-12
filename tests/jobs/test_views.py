from django.urls import reverse, resolve
from parameterized import parameterized
from ..test_class_base import TestBase
from jobs.views import (HomePage, JobOffersList, CreateOfferView, EditOffer, DetailOffer,
                     DeleteOffer, MyOffers, PopularOffers)
from django.utils import timezone


class TestViewClassIsCorrect(TestBase):
    @parameterized.expand([
        (reverse("homepage"), HomePage),
        (reverse("job_list"), JobOffersList),
        (reverse("create_offer"), CreateOfferView),
        (reverse("update_offer", args=(1, )), EditOffer),
        (reverse("detail_offer", args=(1, )), DetailOffer),
        (reverse("delete_offer", args=(1, )), DeleteOffer),
        (reverse("my_offers"), MyOffers),
        (reverse("popular_offers"), PopularOffers)
    ])
    def test_view_class_is_correct(self, url, class_name):
        view = resolve(url).func.view_class
        self.assertIs(view, class_name)


class TestTemplatesInViews(TestBase):
    def setUp(self):
        self.offer = self.create_object_job_offer()
        self.client.login(username="testuser", password="testpassword")

    @parameterized.expand([
        (reverse("homepage"), "homepage.html"),
        (reverse("job_list"), "job_list.html"),
        (reverse("create_offer"), "create_offer.html"),
        (reverse("update_offer", args=(1,)), "update_offer.html"),
        (reverse("detail_offer", args=(1,)), "detail_offer.html"),
        (reverse("delete_offer", args=(1, )), "delete_offer.html"),
        (reverse("my_offers"), "my_offers.html"),
        (reverse("popular_offers"), "popular_offers.html")
    ])
    def test_views_template_return(self, url, template_name):
        response = self.client.get(url)
        self.assertTemplateUsed(response, template_name)


class TestStatusCodeAndRedirectUrlProtectedViews(TestBase):
    @parameterized.expand([
        (reverse("create_offer"), 302),
        (reverse("update_offer", args=(1, )), 302),
        (reverse("delete_offer", args=(1, )), 302),
        (reverse("my_offers"), 302)
    ])
    def test_status_code_returned_by_protected_views(self, url, expected_status_code):
        response = self.client.get(url)
        self.assertEqual(response.status_code, expected_status_code)


class TestProtectedViewsRedirect(TestBase):
    @parameterized.expand([
        (reverse("create_offer")),
        (reverse("update_offer", args=(1, ))),
        (reverse("delete_offer", args=(1, ))),
        (reverse("my_offers"))
    ])
    def test_procted_views_redirect_url_login(self, view_url):
        login_url = f"/login/?next={view_url}"
        response = self.client.get(view_url, follow=True)
        self.assertRedirects(response, login_url)


class TestStatusCodeWhenNotFound(TestBase):
    def setUp(self):
        user_password = "teste"
        user = self.create_test_user()
        self.client.login(username=user.username, password=user_password)

    @parameterized.expand([
        (reverse("update_offer", args=(1, ))),
        (reverse("detail_offer", args=(1, ))),
        (reverse("delete_offer", args=(1, )))
    ])
    def test_status_code_view_when_not_found(self, url):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class TestMyOffersSearch(TestBase):
    def test_my_offers_search(self):
        self.user = self.create_test_user(username="testando", password="testando22")
        self.offer = self.create_object_job_offer(title="Desenvolvedor Python", autor=self.user, allowed=1)
        self.offer = self.create_object_job_offer(title="Desenvolvedor JavaScript", allowed=1)
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("my_offers"), {"search": "JavaScript"})
        self.assertContains(response, "Desenvolvedor JavaScript")
        self.assertNotContains(response, "Desenvolvedor Python")


class TestCreateOfferViewInputInForm(TestBase):
    def setUp(self):
        self.user = self.create_test_user()
        self.offer = self.create_object_job_offer(autor=self.user)
        return super().setUp()

    def test_create_offer_view_autor_in_form(self):
        self.assertIs(self.offer.autor, self.user)

    def test_create_offer_view_email_in_form(self):
        user_email = self.user.email
        self.assertEqual(self.offer.recruiter_email, user_email)


class TestDeleteOfferGetMethod(TestBase):
    def test_delete_offer_get_method_loads_offer_by_autor(self):
        self.offer = self.create_object_job_offer(title="Desenvolvedor JS")
        self.client.login(username="testuser", password="testpassword")  # Credenciais do usuario criado no metodo de criar offer
        response = self.client.get(reverse("delete_offer", args=(self.offer.pk, )))
        self.assertContains(response, self.offer.title)

    def test_delete_offer_dont_loads_offer_if_not_autor(self):
        random_user = self.create_test_user(username="randomuser", password="randomuser")
        offer = self.create_object_job_offer(title="Desenvolvedor Golang")
        self.client.login(username=random_user.username, password="randomuser")
        response = self.client.get(reverse("delete_offer", args=(offer.pk, )))
        self.assertRedirects(response, reverse("job_list"))


class TestJobOffersListSearch(TestBase):
    def setUp(self):
        self.offer = self.create_object_job_offer(title="Desenvolvedor JavaScript")

    def test_job_offers_list_search(self):
        response = self.client.get(reverse("job_list"), {"search": "Python"})
        self.assertNotContains(response, "Desenvolvedor JavaScript")


class TestEditOfferGetMethod(TestBase):
    def test_edit_offer_get_method_loads_offer_by_autor(self):
        """
        Testa se ao criar uma oferta a pagina edit_offer carrega a oferta corretamente
        quando o usuário logado é o autor da oferta
        """
        self.offer = self.create_object_job_offer(title="Desenvolvedor Java")  # Cria uma oferta
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("update_offer", args=(1, )))
        self.assertContains(response, self.offer.title)

    def test_edit_offer_get_method_dont_loads_offer_by_others(self):
        """Testa se quando um usuario que não é o autor de uma oferta acessa a url
        é redirecionado para job_list"""
        random_user = self.create_test_user(username="teste", password="teste")
        user_autor = self.create_test_user(username="testando...", password="testando...")
        self.offer = self.create_object_job_offer(title="Desenvolvedor .NET", autor=user_autor)
        self.client.login(username=random_user.username, password="teste")
        response = self.client.get(reverse("update_offer", args=(self.offer.id, )))
        self.assertRedirects(response, reverse("job_list"))


class TestViewsRedirectForSuccessUrl(TestBase):
    def setUp(self):
        self.user = self.create_test_user()
        self.offer_data = {
            'title': "Desenvolvedor Full Stack",
            'description': "Descrição da vaga de desenvolvedor Full Stack.",
            'organization_name': "Empresa ABC",
            'location': "Cidade XYZ",
            'publication_date': timezone.now(),  # Usando a hora atual
            'offer_requirements': "Requisitos da vaga.",
            'employment_type': "Tempo Integral",
            'salary': 8000,
            'organization_description': "Descrição da organização.",
            'autor': 1,
            'recruiter_email': "recruiter@example.com",
            'number_of_views': 0
        }
        return super().setUp()

    def test_create_offer_success_url_redirect(self):
        user_password = "teste"
        success_url = reverse("my_offers")  # URL de redirecionamento em caso de sucesso
        self.client.login(username=self.user.username, password=user_password)
        response = self.client.post(reverse("create_offer"), data=self.offer_data, follow=True)
        self.assertRedirects(response, success_url)


class TestViewsDontLoadsOffersWithAllowedZero(TestBase):
    def setUp(self):
        self.offer = self.create_object_job_offer(title="Dev Salesforce", allowed=0)  # Cria uma oferta com allowed zero
        self.client.login(username="testuser", password="testpassword")
    @parameterized.expand([
        (reverse("job_list")),
        (reverse("my_offers")),
        (reverse("popular_offers"))])
    def test_views_dont_loads_offers_with_allowed_zero(self, url):
        response = self.client.get(url)
        self.assertNotContains(response, "Dev Salesforce")


class TestJobOffersListTotalOffers(TestBase):
    def test_job_offers_view_return_correct_total_of_offers(self):
        self.offer = self.create_object_job_offer(allowed=1)
        response = self.client.get(reverse("job_list"))
        offers_returned = response.context["object_list"].count()  # Total de ofertas retornadas pelo queryset da view
        total_offers_found = response.context["total_offers_found"]  # Valor da variavel total_offers_found
        self.assertEqual(offers_returned, total_offers_found)


class TestPopularOffersQuerysetOrder(TestBase):
    def test_popular_offers_queryset_order(self):
        user = self.create_test_user("testando", "testando")
        for i in range(3):
            offer = self.create_object_job_offer(title=f"Desenvolvedor {i}", autor=user, allowed=1)
            offer.number_of_views = i  # Atribui ao numero de views da oferta o valor de i
            offer.save()
        response = self.client.get(reverse("popular_offers"))
        queryset = response.context["joboffer_list"]
        self.assertEqual(queryset[0].title,  "Desenvolvedor 2")  # Verifica se o 1 do queryset é o desenvolvedor2


class TestViewsPagination(TestBase):
    def setUp(self):
        autor_password = "testando"
        self.user = self.create_test_user("testando", password=autor_password)
        for i in range(10):
            self.offer = self.create_object_job_offer(title=f"Desenvolvedor {i}", autor=self.user, allowed=1)
        self.client.login(username=self.user.username, password=autor_password)
    @parameterized.expand([
        (reverse("job_list")),
        (reverse("my_offers")),
        (reverse("popular_offers"))
    ])
    def test_if_pagination_in_views_is_working_correct(self, url):
        response = self.client.get(url)
        paginator = response.context["paginator"]
        self.assertEqual(paginator.num_pages, 2)
