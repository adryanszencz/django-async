import asyncio
import time

from django.http import HttpResponse


def tarefa_sincrona(numero):
    print(f"Iniciando tarefa {numero}")
    time.sleep(1)
    print(f"Tarefa {numero} concluída")


async def tarefa_assincrona(numero):
    print(f"Iniciando tarefa {numero}")
    await asyncio.sleep(1)
    print(f"Tarefa {numero} concluída")


def view_sincrona(request):
    """View tradicional: as 5 tarefas rodam uma depois da outra (~5 s)."""
    inicio = time.perf_counter()
    for numero in range(1, 6):
        tarefa_sincrona(numero)
    tempo = time.perf_counter() - inicio
    print(f"View síncrona levou {tempo:.2f} s")
    return HttpResponse(f"View síncrona: 5 tarefas em {tempo:.2f} s")


async def view_assincrona(request):
    """Async view: as 5 tarefas esperam juntas com asyncio.gather (~1 s)."""
    inicio = time.perf_counter()
    await asyncio.gather(*(tarefa_assincrona(numero) for numero in range(1, 6)))
    tempo = time.perf_counter() - inicio
    print(f"View assíncrona levou {tempo:.2f} s")
    return HttpResponse(f"View assíncrona: 5 tarefas em {tempo:.2f} s")
