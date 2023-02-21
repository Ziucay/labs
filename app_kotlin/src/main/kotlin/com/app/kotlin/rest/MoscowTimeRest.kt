package com.app.kotlin.rest

import com.app.kotlin.model.MoscowTimeRestDTO
import com.app.kotlin.service.GetTimeService
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RestController

@RestController
class MoscowTimeRest(private val getTimeService: GetTimeService) {

    @GetMapping("/moscow/time")
    fun moscowTime(): MoscowTimeRestDTO {
        return MoscowTimeRestDTO(getTimeService.getMoscowTime())
    }
}
