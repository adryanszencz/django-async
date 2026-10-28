import asyncio
import time

import pytest
from django.urls import reverse

from core import views


def test_view_assincrona_e_coroutine():
    assert asyncio.iscoroutinefunction(views.view_assincrona)


@pytest.mark.asyncio
async def test_view_assincrona_roda_as_tarefas_juntas(async_client):
    inicio = time.perf_counter()
    response = await async_client.get(reverse("async"))
    tempo = time.perf_counter() - inicio

    assert response.status_code == 200
    assert "View assíncrona" in response.content.decode()
    # 5 tarefas de 1 s esperando juntas levam ~1 s, não 5 s
    assert tempo < 2.5


def test_view_sincrona(client):
    response = client.get(reverse("sync"))

    assert response.status_code == 200
    assert "View síncrona" in response.content.decode()
